import os, sys
import networkx as nx
import pylab
import GafoEu as Eu

#creamos el grafico en blanco
flag = False
G = nx.Graph()
G2 = nx.Graph()
nodosRutaOptima = []
pylab.figure("Grafico Dirigido")

#Esta funcion regresa una lista de Nodos, cada nodo se conforma
# por nodopartida, nodollegada, distancia
def leerTXTNodos():
    text_file = open("ListaNodos4.txt", "r")
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


def leerTXTHeuristica(cantidadNodos):
    text_file = open("Heuristica.txt", "r")
    lines = text_file.read().replace('\n', ',').split(',')
    text_file.close()

    listaNodos = []
    nodo = []
    
    for x in range(len(lines)):
        pos = x % cantidadNodos
        
        if pos == (cantidadNodos -1):
            
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
    nx.draw_networkx_edges(grafo,pos, width=2.2, font_color="b")
    nx.draw_networkx_edge_labels(grafo,pos)

def obtenerEuristica(heurisitica,final):

    tablaHeuristica = []
    contador = 0
    for x in heurisitica[0]:
        if x == final:
            tablaHeuristica = [heurisitica[0],heurisitica[contador +1 ]]
        else:
            contador +=1
    return tablaHeuristica

def creadorRuta(listaRutas,tablaEuristica,ListaNodos,final):
    
    rutas = []
    menor = 0
    cont = 0

    for x in range(len(listaRutas)):
        if menor == 0:
            menor = listaRutas[x][0]
            cont = x
        elif menor > listaRutas[x][0]:
            menor = listaRutas[x][0]
            cont = x

    print(listaRutas)    
    print(listaRutas[cont][1][-1])
    if listaRutas[cont][1][-1] != final:
        
        vecinos = G.neighbors(listaRutas[cont][1][-1])
        print("nodo: " + listaRutas[cont][1][-1])

        for x in vecinos:
            
            print("vecionos: " + x)
            peso = 0

            
            peso = int(listaRutas[cont][0]) + int(G[listaRutas[cont][1][-1]][x].get("KM"))+ int(tablaEuristica[1][tablaEuristica[0].index(x)])
            
            ruta = listaRutas[cont][1].copy()
            ruta.append(x)

            listaRutas.append([peso,ruta])

        listaRutas.pop(cont)
        print(flag)
    
        return(listaRutas)
    
    elif listaRutas[cont][1][-1] == final and menor == listaRutas[cont][0]:
        flag == True
        print(flag)
    
        return(listaRutas[cont][1][-1])

def procesar(tablaEuristica,ListaNodos,inicial,final):
    cont = 0
    listaRutas = []


    for x in tablaEuristica[0]:
        if x == inicial:
            listaRutas = [[tablaEuristica[1][cont] , [tablaEuristica[0][cont] ]] ]
        else:
            cont +=1
    while flag == False:
        listaRutas = creadorRuta(listaRutas,tablaEuristica,ListaNodos,final)

    print(listaRutas)
    

def AlgoritmoA(heurisitica,ListaNodos,inicial,final):

    tablaEuristica = obtenerEuristica(heurisitica,final)
    procesar(tablaEuristica,ListaNodos,inicial,final)
    
    
    
    

#ejecucion
    
listaNodosInicial = leerTXTNodos()
agregarNodosGraficos(listaNodosInicial)
agregarNodosGraficosMejorRuta(listaNodosInicial[:3])

#Instrucciones para imprimir el grafico
pos = nx.spring_layout(G)
imprimirGrafico(G,"g")

#LLamado a leer la Heuristica
cantidadNodos = len(G.nodes())
heuristica = leerTXTHeuristica(cantidadNodos)

rutaOptima = AlgoritmoA(heuristica, listaNodosInicial,"Heredia","Cartago")

imprimirGrafico(G2,"b")

#Muestra el grafico
pylab.show()

