from BinaryTree import BinaryTree
from NodeT import Node
from BSTEntry import BSTEntry
class BinarySearchTree(BinaryTree):
    
    def insert(self, key, data):
        new_entry = BSTEntry(data, key)
        if self.root is None:
            self.root = Node(new_entry)
            self.size = 1
            return
        
        current = self.root
        while True:
            if key < current.getData().getKey():
                if current.getLeft() is None:
                    current.setLeft(Node(new_entry))
                    break
                current = current.getLeft()
            else:
                if current.getRight() is None:
                    current.setRight(Node(new_entry))
                    break
                current = current.getRight()
        self.size += 1
    
    def min(self, node):
        if self.has_left(node):
            return self.min(self.left(node))
        return node.getData()

    def max(self, node):
        if self.has_right(node):
            return self.max(self.right(node))
        return node.getData()
    
    def find(self, key):
        return self.search_tree(key, self.root)

    def search_tree(self, key, node):
        if node is None:
            return None
        
        entry = node.getData()
        if key == entry.getKey():
            return node
        elif key < entry.getKey():
            return self.search_tree(key, node.getLeft())
        else:
            return self.search_tree(key, node.getRight())
        
    def remove(self, key):
        node = self.find(key)
        if node is None:
            return None

        temp = node.getData()

        if self.has_left(node) and self.has_right(node):  # Caso 2
            pred = self.predecessor(node)
            node.setData(pred.getData())
            super().remove(pred)
        else:  # Caso 1
            super().remove(node)

        return temp

    def predecessor(self, node):
        temp = node.getLeft()
        return self.maxNode(temp)

    def maxNode(self, node):
        if self.has_right(node):
            return self.maxNode(self.right(node))
        return node
    
    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node is not None:
            
            if self.has_left(node):
                self._inorder_helper(node.getLeft(), result)

            result.append(node.getData().getKey())
            
            if self.has_right(node):
                self._inorder_helper(node.getRight(), result)

    def mostrarArbol(self):
        """Muestra el árbol de manera visual en formato horizontal."""
        self.mostrarArbolAux(self.root, 0)

    def mostrarArbolAux(self, node, level):
        """Método auxiliar recursivo para mostrar el árbol."""
        if node is not None:
            # Recorre el subárbol derecho primero
            self.mostrarArbolAux(node.getRight(), level + 1)
            
            # Imprime el nodo actual con sangría proporcional al nivel
            print(' ' * 4 * level + '->', node.getData().getKey())
            
            # Recorre el subárbol izquierdo
            self.mostrarArbolAux(node.getLeft(), level + 1)
