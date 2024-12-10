import DoubleList
import DoubleNode
numerospares = DoubleList()
i=2
while i <= 20:
    if i % 2 == 0:    
        if i == 2:
            numerospares.addFirst(i)
            i += 1
        else:
            numerospares.addLast(i)
            i += 1
    else:
        i += 1

print(numerospares.first().getData())
#temp = numerospares.first()
#j = numerospares.size()
#for k in range(j):
#    print(temp.getNext().getData())
#    temp = temp.getNext()