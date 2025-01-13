from Usuario import Usuario
from DoubleList import DoubleList
from Fecha import Fecha
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
print(coleccion_usuarios.first().getData())
temp = coleccion_usuarios.first()
k = coleccion_usuarios.size()

for l in range(k-1):
        print(temp.getNext().getData())
        temp = temp.getNext()

def pedirUsuario():
    nombre = input('Introduzca su nombre: ')
    id = input('Introduzca su Id: ')
    dd = input('Introduzca su día de nacimiento: ')
    mm = input('Introduzca su mes de nacimiento: ')
    aa = input('Introduzca su año de nacimiento: ')
    ciudad_nacimiento = input('Introduzca su ciudad de nacimiento: ')
    telefono = input('Introduzca su télefono: ')
    email = input('Introduzca su email: ')
    verificador = input('¿Desea introducir su dirección? Responda SI o NO: ')
    new_usuario = Usuario(nombre, id)
    fecha_usuario = Fecha(dd,mm,aa)
    new_usuario.setCiudad_nacimiento(ciudad_nacimiento)
    new_usuario.setTel(telefono)
    new_usuario.setEmail(email)
    if verificador == "SI":
         calle = input("Introduzca su calle: ")
         nomenclatura = input("Introduzca su nomenclatura: ")
         barrio = input("Introduzca su barrio: ")
         ciudad = input("Introduzca su ciudad: ")
         edificio = input("Introduzca su edificio: ")
         apto = input("Introduzca su apartamento, si no aplica déjelo vacío: ")
         new_usuario.getDir().setAll(calle, nomenclatura, barrio, ciudad, edificio, apto)

    return new_usuario

coleccion_usuarios.addFirst(pedirUsuario())
coleccion_usuarios.addLast(pedirUsuario())

print(coleccion_usuarios.first().getData())
temp = coleccion_usuarios.first()
k = coleccion_usuarios.size()

for l in range(k-1):
        print(temp.getNext().getData())
        temp = temp.getNext()

def Insertar(posicion, DoubleList, Dato):
    tempAux = coleccion_usuarios.first()
    posicion = coleccion_usuarios.size()

    for l in range(posicion-1):
            tempAux = tempAux.getNext() 
    DoubleList.addBefore(tempAux,Dato)

Insertar(3,coleccion_usuarios, pedirUsuario())

print(coleccion_usuarios.first().getData())
temp = coleccion_usuarios.first()
k = coleccion_usuarios.size()

for l in range(k-1):
        print(temp.getNext().getData())
        temp = temp.getNext()







