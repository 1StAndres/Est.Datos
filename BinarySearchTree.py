from BinaryTree import BinaryTree 
from BinaryTree import Node
from BSTEntry import BSTEntry
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, key, value):
        entry = BSTEntry(key, value)
        if self.root is None:
            self.root = Node(entry)
        else:
            self._insert(self.root, entry)

    def _insert(self, node, entry):
        if entry.key < node.entry.key:
            if node.left is None:
                self.insertLeft(node, entry)
            else:
                self._insert(node.left, entry)
        else:
            if node.right is None:
                self.insertRight(node, entry)
            else:
                self._insert(node.right, entry)

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None or node.entry.key == key:
            return node
        elif key < node.entry.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.entry.key:
            node.left = self._remove(node.left, key)
        elif key > node.entry.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._findMin(node.right)
                node.entry = successor.entry
                node.right = self._remove(node.right, successor.entry.key)
        return node

    def _findMin(self, node):
        while node.left is not None:
            node = node.left
        return node

    def findMax(self):
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.entry

    def findMin(self):
        if self.root is None:
            return None
        node = self.root
        while node.left is not None:
            node = node.left
        return node.entry

    def display(self):
        self._display(self.root, 0)

    def _display(self, node, level):
        if node is not None:
            self._display(node.right, level + 1)
            print(' ' * 4 * level + '->', node.entry)
            self._display(node.left, level + 1)

    def inorderTraversal(self):
        self.inorder(self.root, lambda entry: print(entry))
