from Usuario import Usuario
from DoubleList import DoubleList
import DoubleNode

i = 2
numeros_pares = DoubleList()
while (i <= 20):
    numeros_pares.addLast(i)
    i += 2 

print(numeros_pares.first().getData())
temp = numeros_pares.first()
j = numeros_pares.size()

for k in range(j-1):
        print(temp.getNext().getData())
        temp = temp.getNext()

coleccion_usuarios = DoubleList()
coleccion_usuarios.addLast(Usuario("Gerardo",1002346789))
coleccion_usuarios.addLast(Usuario("Bernardo",1002396389))
coleccion_usuarios.addLast(Usuario("Rigoberto",1001346789))
coleccion_usuarios.addLast(Usuario("Alberto",1002476789))
coleccion_usuarios.addLast(Usuario("Antonio",1234346789))
print(coleccion_usuarios.first())
temp = coleccion_usuarios.first()
k = coleccion_usuarios.size()

for l in range(j-1):
      print(temp.getNext().getData())
      temp = temp.getNext()