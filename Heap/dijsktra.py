from heap2 import *
from Grafo import *

def initializeSingleSource(H,s):
    for u in H.vertices:
        u.d = 99999999
        u.pi = None
    s.d = 0

def relax(u,v):
    if v[0].d > u.d + v[1]:
        v[0].d = u.d + v[1]
        v[0].pi = u

def Dijkstra(G,s):
    #Inicializacion
    initializeSingleSource(G,s)
    H = G.vertices.copy()
    min_heapify(H)
    while len(H)!=0:
        u = extract_min(H)
        for v in u.vecinos:
            relax(u,v)

#Carga del grafo
vertics = [Vertice("s"),Vertice("t"),Vertice("y"),Vertice("x"),Vertice("z")]
grafo = Grafo()
grafo.vertices = vertics
grafo.agregarArista(vertics[0],[vertics[1],10])
grafo.agregarArista(vertics[0],[vertics[2],5])
grafo.agregarArista(vertics[1],[vertics[2],2])
grafo.agregarArista(vertics[1],[vertics[3],1])
grafo.agregarArista(vertics[2],[vertics[1],3])
grafo.agregarArista(vertics[2],[vertics[3],7])
grafo.agregarArista(vertics[2],[vertics[4],2])
grafo.agregarArista(vertics[3],[vertics[4],4])
grafo.agregarArista(vertics[4],[vertics[3],6])
grafo.mostrarVecinos()
Dijkstra(grafo,grafo.vertices[0])
print("")
grafo.mostrarPadres()
grafo.mostrarGrafoSimplificado()
