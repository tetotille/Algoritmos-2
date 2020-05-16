from heap2 import *
from Grafo import *

def initializeSingleSource(H,s):
    for u in H.vertices:
        u.d = float("inf")
        u.pi = None
    s.d = 0

def relax(u,lista,i,key):
    if lista[i][0].d > key:
        lista[i][0].pi = u
        heap_decrease_key(lista,i,key)

def Dijkstra(G,s):
    initializeSingleSource(G,s)
    H = G.vertices.copy()
    min_heapify(H)
    while len(H)!=0:
        u = extract_min(H)
        for i in range(len(u.vecinos)):
            v = u.vecinos[i]
            relax(u,u.vecinos,i,u.d+v[1])


if __name__ != "__main__":
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
    print("NO")
if __name__ == "__main__":
    vertics = [Vertice("1"),Vertice("2"),Vertice("3"),Vertice("4"),Vertice("5")]
    grafo = Grafo()
    grafo.vertices = vertics
    grafo.agregarArista(vertics[0],[vertics[1],1])
    grafo.agregarArista(vertics[0],[vertics[3],3])
    grafo.agregarArista(vertics[0],[vertics[4],100])
    grafo.agregarArista(vertics[1],[vertics[2],5])
    grafo.agregarArista(vertics[2],[vertics[4],1])
    grafo.agregarArista(vertics[3],[vertics[2],2])
    grafo.agregarArista(vertics[3],[vertics[4],6])
    grafo.mostrarVecinos()
    Dijkstra(grafo,grafo.vertices[0])
    print("")
    grafo.mostrarVecinos()
    grafo.mostrarGrafoSimplificado()
