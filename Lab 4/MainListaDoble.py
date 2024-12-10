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