import os, sys
import networkx as nx
import pylab

#creamos el grafico en blanco

G = nx.Graph()
G2 = nx.Graph()
pylab.figure("Grafico Dirigido")

#Esta funcion regresa una lista de Nodos, cada nodo se conforma
# por nodopartida, nodollegada, distancia
def leerTXTNodos():
    text_file = open("ListaNodos.txt", "r")
    lines = text_file.read().replace('\n', ',').split(',')
    text_file.close()

    listaNodos = []
    nodo = []
    
    for x in range(len(lines)):
        pos = x % 3
        
        if pos == 2:
            
            nodo.append(lines[x])
            listaNodos.append(nodo)
            nodo = []
            
        else:
            
            nodo.append(lines[x])

    return listaNodos


def leerTXTHeuristica():
    text_file = open("Heuristica.txt", "r")
    lines = text_file.read().replace('\n', ',').split(',')
    text_file.close()

    listaNodos = []
    nodo = []
    
    for x in range(len(lines)):
        pos = x % 3
        
        if pos == 2:
            
            nodo.append(lines[x])
            listaNodos.append(nodo)
            nodo = []
            
        else:
            
            nodo.append(lines[x])

    return listaNodos



def agregarNodosGraficos(listaNodos):   
    #G.add_edge("Estacion 3", "Estacion 1", V = 33.5)
    for x in listaNodos:
        G.add_edge(x[0], x[1], KM = x[2])

def agregarNodosGraficosMejorRuta(listaNodos):   
    #G.add_edge("Estacion 3", "Estacion 1", V = 33.5)
    for x in listaNodos:
        G2.add_edge(x[0], x[1], KM = x[2])
        
    
def imprimirGrafico(grafo, color):
    
    nx.draw_networkx_nodes(grafo, pos, node_color = color)
    nx.draw_networkx_labels(grafo, pos)
    nx.draw_networkx_edges(grafo,pos, width=1.2, font_color="b")
    nx.draw_networkx_edge_labels(grafo,pos)
        

#ejecucion
    
listaNodosInicial = leerTXTNodos()
agregarNodosGraficos(listaNodosInicial)
agregarNodosGraficosMejorRuta(listaNodosInicial[:3])


#Instrucciones para imprimir el grafico
pos = nx.spring_layout(G)
imprimirGrafico(G,"g")
imprimirGrafico(G2,"b")

#Muestra el grafico
pylab.show()

