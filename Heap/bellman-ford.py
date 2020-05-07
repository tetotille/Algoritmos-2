from dag import initializeSingleSource, relax
from Grafo import *

def bellman_ford(G,s):
    initializeSingleSource(G,s)
    for i in range(len(G.vertices)):
        for u in G.vertices:
            for v in u.vecinos:
                relax(u,v)
    for u in G.vertices:
        for v in u.vecinos:
            if u.d > u.d + v[1]:
                return False
    return True

if __name__ == "__main__":
    vertics = [Vertice("s"),Vertice("t"),Vertice("y"),Vertice("x"),Vertice("z")]
    grafo = Grafo()
    grafo.vertices = vertics
    grafo.agregarArista(vertics[0],[vertics[1],6])
    grafo.agregarArista(vertics[0],[vertics[2],7])
    grafo.agregarArista(vertics[1],[vertics[2],8])
    grafo.agregarArista(vertics[1],[vertics[3],5])
    grafo.agregarArista(vertics[1],[vertics[4],-4])
    grafo.agregarArista(vertics[2],[vertics[3],-3])
    grafo.agregarArista(vertics[2],[vertics[4],9])
    grafo.agregarArista(vertics[3],[vertics[1],-2])
    grafo.agregarArista(vertics[4],[vertics[0],2])
    grafo.agregarArista(vertics[4],[vertics[3],7])
    grafo.mostrarVecinos()
    bellman_ford(grafo,grafo.vertices[0])
    print("")
    grafo.mostrarVecinos()
    grafo.mostrarGrafoSimplificado()
