import networkx as nt
import pandas as pd

def CaminoMasCortoTiempo(ciuA, ciuB, g):
    return  nt.dijkstra_path(g, ciuA, ciuB, weight = "tiempo")


url = "https://raw.githubusercontent.com/1StAndres/Est.Datos/refs/heads/main/Datos%20vias.csv"
dataset = pd.read_csv(url, delimiter=';', skiprows=1, names=['CiudadA', 'CiudadB', 'KM', 'Minutos'])
grafo = nt.Graph()

for _, row in dataset.iterrows():
    grafo.add_edge(row['CiudadA'], row['CiudadB'], distancia=row['KM'], tiempo=row['Minutos'])

a = input("Ingrese el nombre de la primera ciudad: ")
b = input("Ingrese el nombre de la segunda ciudad: ")
rutaT = CaminoMasCortoTiempo(a, b ,grafo) #¿no debería ser entre a y b?
print(f"La ruta mas corta segun el tiempo desde la ciudad {a} y la ciudad {b} es: {rutaT}")


#Función ¿están conectadas por una sola carretera?
def estan_conectadas(ciuA, ciuB, g):
    return g.has_edge(ciuA, ciuB)
print("¿Están conectadas por una sola carretera?")
x = input("Ingrese la primera ciudad: ")
y = input("Ingrese la segunda ciudad: ")

if estan_conectadas(x, y, grafo):
    print(f"{x} y {y} están conectadas directamente por una carretera.")
else:
    print(f"{x} y {y} NO están conectadas directamente.")
