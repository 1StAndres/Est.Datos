class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def root(self):
        return self.root

    def left(self, v):
        return v.left

    def right(self, v):
        return v.right

    def hasLeft(self, v):
        return v.left is not None

    def hasRight(self, v):
        return v.right is not None

    def isRoot(self, v):
        return v == self.root

    def isInternal(self, v):
        return self.hasLeft(v) or self.hasRight(v)

    def addRoot(self, e):
        if self.root is not None:
            raise ValueError("Ya existe una raiz")
        self.root = Node(e)
        self.size = 1
        return self.root

    def insertLeft(self, v, e):
        if self.hasLeft(v):
            raise ValueError("Ya existe hijo izquierdo")
        v.left = Node(e)
        self.size += 1
        return v.left

    def insertRight(self, v, e):
        if self.hasRight(v):
            raise ValueError("Ya existe hijo derecho")
        v.right = Node(e)
        self.size += 1
        return v.right

    def remove(self, v):
        if self.hasLeft(v) and self.hasRight(v):
            raise ValueError("El nodo tiene dos hijos")
        child = v.left if self.hasLeft(v) else v.right
        if self.isRoot(v):
            self.root = child
        else:
            # Para eliminar un nodo, necesitamos encontrar su padre.
            # Sin un puntero al padre, esto requiere un recorrido del árbol.
            parent = self._findParent(self.root, v)
            if parent.left == v:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        return v.value

    def _findParent(self, current, v):
        # Método auxiliar para encontrar el padre de un nodo.
        if current is None:
            return None
        if current.left == v or current.right == v:
            return current
        parent = self._findParent(current.left, v)
        if parent is not None:
            return parent
        return self._findParent(current.right, v)

    def depth(self, v):
        # Sin un puntero al padre, la profundidad debe calcularse recorriendo el árbol.
        return self._depth(self.root, v, 0)

    def _depth(self, current, v, current_depth):
        if current is None:
            return -1
        if current == v:
            return current_depth
        left_depth = self._depth(current.left, v, current_depth + 1)
        if left_depth != -1:
            return left_depth
        return self._depth(current.right, v, current_depth + 1)

    def height(self, v):
        if not self.isInternal(v):
            return 0
        else:
            left_height = self.height(v.left) if self.hasLeft(v) else 0
            right_height = self.height(v.right) if self.hasRight(v) else 0
            return 1 + max(left_height, right_height)
