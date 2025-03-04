import networkx as nt
import pandas as pd

url = "https://raw.githubusercontent.com/1StAndres/Est.Datos/refs/heads/main/Datos%20vias.csv"
dataset = pd.read_csv(url, delimiter=';', skiprows=1, names=['CiudadA', 'CiudadB', 'KM', 'Minutos'])
grafo = nt.Graph()

for _, row in dataset.iterrows():
    grafo.add_edge(row['CiudadA'], row['CiudadB'], distancia=row['KM'], tiempo=row['Minutos'])
