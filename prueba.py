# -*- coding: latin-1 -*-
import os, sys

#Grafo ponderado con GML

import networkx as nx

import pylab

#creamos el grafo y leemos de una ves el archivo gml,

#ojo debes crear este archivo en la misma carpeta

G = nx.read_gml('emp2.txt')
G2 = nx.read_gml('emp2.txt')


#Agregamos mas conexiones

G.add_edge("Estacion 4", "Estacion 1", V = 0)

G.add_edge("Estacion 4", "Estacion 3", V = 93.4)

G.add_edge("Estacion 4", "Estacion 2", V = 53.5)

G.add_edge("Estacion 2", "Estacion 1", V = 43.2)

G.add_edge("Estacion 3", "Estacion 1", V = 33.5)

G.add_edge("Estacion 1", "Estacion 5", V = 13.4)

G.add_edge("Estacion 5", "Estacion 6", V= 78.5)

G.add_edge("Estacion 6", "Estacion 7", V= 48.5)

G.add_edge("Estacion 5", "Estacion 7", V= 18.5)

G.add_edge("Estacion 0", "Estacion 4", V= 18.5)

pos=nx.spring_layout(G)

pos=nx.spring_layout(G)


# Nombre del Grafo

pylab.figure("Mi Grafo")

nx.draw_networkx_nodes(G, pos, node_color = "b")
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_nodes(G2, pos, node_color = "r")
nx.draw_networkx_labels(G2, pos)
nx.draw_networkx_edges(G,pos, width=1.2, font_color="b")
nx.draw_networkx_edge_labels(G,pos)

# ver el grafo llamado figure1

pylab.show()
