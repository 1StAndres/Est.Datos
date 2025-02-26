from BinarySearchTree import BinarySearchTree
# en proceso Pd mostrar el arbol lo hizo chatgpt soy una mrd manejando cadenas de texto si lo saben hacer mejor bien puesdan XD
def calculate_key(id_number):
    return sum(int(digit) for digit in str(id_number))

bst = BinarySearchTree()

users = [
    ("Juan", "10101013"),
    ("Pablo", "10001011"),
    ("Maria", "10101015"),
    ("Ana", "1010000"),
    ("Diana", "10111105"),
    ("Mateo", "10110005")
]

for name, id_number in users:
    key = calculate_key(id_number)
    bst.insert(key, (name, id_number))

print("\nÁrbol Binario de Búsqueda:")
bst.mostrarArbol()


#from BinarySearchTree import BinarySearchTree

# Crear árbol BST
# bst = BinarySearchTree()

# Insertar elementos
# bst.insert(50, "A")
# bst.insert(30, "B")
# bst.insert(70, "C")
# bst.insert(20, "D")
# bst.insert(40, "E")
# bst.insert(60, "F")
# bst.insert(80, "G")

# Mostrar árbol
# print("Árbol inicial:")
# bst.mostrarArbol()

# Buscar elementos
print("\nBuscar 40:", bst.find(4))
print("Buscar 100 (no existe):", bst.find(100))

# Mínimo y máximo
print("\nValor mínimo:", bst.min(bst.getRoot()))
print("Valor máximo:", bst.max(bst.getRoot()))

# Recorrido inorder
print("\nRecorrido inorder:", bst.inorder_traversal())

# Eliminar nodo con 2 hijos
# print("\nEliminar nodo 50 (con 2 hijos)")
# bst.remove(9)
# bst.mostrarArbol()

# # Eliminar nodo hoja
# print("\nEliminar nodo 20 (hoja)")
# bst.remove(20)
# bst.mostrarArbol()

# # Eliminar nodo con un solo hijo
# print("\nEliminar nodo 30 (con un hijo)")
# bst.remove(30)
# bst.mostrarArbol()

