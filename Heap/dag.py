from Grafo import *

def initializeSingleSource(H,s):
    for u in H.vertices:
        u.d = 99999999
        u.pi = None
    s.d = 0

def topological_sort(G):
    lista = G.DFS()
    return lista[::-1]

def relax(u,v):
    if v[0].d > u.d + v[1]:
        v[0].d = u.d + v[1]
        v[0].pi = u

def imprimir(lista):
    for u in lista:
        print(u)

def dag_shortest_paths(G,s):#El peso ya se incluye en la definición del grafo
    lista_enlazada = topological_sort(G)
    initializeSingleSource(G,s)
    for u in lista_enlazada:
        for v in u.vecinos:
            relax(u,v)


vertics = [Vertice("a"),Vertice("b"),Vertice("c"),Vertice("d"),Vertice("e"),Vertice("f")]
grafo = Grafo()
grafo.vertices = vertics
grafo.agregarArista(vertics[0],[vertics[1],3])
grafo.agregarArista(vertics[0],[vertics[2],1])
grafo.agregarArista(vertics[1],[vertics[3],2])
grafo.agregarArista(vertics[2],[vertics[3],8])
grafo.agregarArista(vertics[2],[vertics[4],4])
grafo.agregarArista(vertics[3],[vertics[4],7])
grafo.agregarArista(vertics[3],[vertics[5],1])
grafo.agregarArista(vertics[4],[vertics[5],5])
grafo.mostrarVecinos()
dag_shortest_paths(grafo,grafo.vertices[0])
print("")
grafo.mostrarVecinos()
grafo.mostrarGrafoSimplificado()
