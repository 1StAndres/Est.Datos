from BinaryTree import BinaryTree
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def find(self, k):
        return self._find(self.root, k)

    def _find(self, node, k):
        if node is None or node.value == k:
            return node
        elif k < node.value:
            return self._find(node.left, k)
        else:
            return self._find(node.right, k)

    def insert(self, e, k):
        if self.root is None:
            self.addRoot(e)
        else:
            self._insert(self.root, e, k)

    def _insert(self, node, e, k):
        if k < node.value:
            if self.hasLeft(node):
                self._insert(node.left, e, k)
            else:
                self.insertLeft(node, e)
        else:
            if self.hasRight(node):
                self._insert(node.right, e, k)
            else:
                self.insertRight(node, e)

    def remove(self, k):
        node = self.find(k)
        if node is None:
            return None
        if self.hasLeft(node) and self.hasRight(node):
            successor = self._findMin(node.right)
            node.value = successor.value
            node = successor
        return super().remove(node)

    def _findMin(self, node):
        while self.hasLeft(node):
            node = node.left
        return node
