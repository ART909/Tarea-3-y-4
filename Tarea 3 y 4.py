import os, sys
import networkx as nx
import pylab

#creamos el grafico en blanco
G = nx.Graph()



def grafricarNodos(listaNodos):
    
    #G.add_edge("Estacion 3", "Estacion 1", V = 33.5)
    for x in ListaNodos:
        G.add_edge(x[0], x[1], x[2])
        
    
