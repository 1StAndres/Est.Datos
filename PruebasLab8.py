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
