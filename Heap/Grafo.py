import networkx as nx
import matplotlib.pyplot as plt

lista_enlazada = []

class Vertice:
    def __init__(self,x):
        self.clave = x
        self.vecinos = []  #lista de adyacencias (lista en lugar de conjunto)
        self.color = None
        self.pi = None
        self.d = None
        self.f = None
    def __str__(self):
        return ("Vertice "+str(self.clave)+ "   Padre: "+str(self.pi))

    def __lt__(self, other):
        if self.clave < other.clave:
            return True
        else:
            return False

    def __eq__(self,other):
        if other == None:
            return self.clave == None
        if self.clave == other.clave:
            return True
        else:
            return False

    def __le__(self,other):
        return self.clave <= other.clave

    def __gt__(self,other):
        return self.clave > other.clave

    def __ge__(self,other):
        return self.clave >= other.clave

    def __ne__(self,other):
        if other == None:
            return self.clave != None
        return self.clave != other.clave


class Grafo:
    def __init__(self):
        self.vertices = []

    def agregarVertice(self, V):
        self.vertices.append(V)

    def agregarArista(self,a,b):
        a.vecinos.append(b)

    def mostrarVecinos(self):
        for u in self.vertices:
            print("Vertice",u.clave,": ",end="")
            for v in u.vecinos:
                print(v[0].clave," ",end="")
            if u.pi != None:
                print("\tPadre: ",u.pi.clave,"\td: ",str(u.d))
            else:
                print("\tPadre: ","None","\td: ",str(u.d))

    def mostrarGrafo(self):
        G = nx.DiGraph()
        for u in self.vertices:
            G.add_node(u.clave) #para mostrar vértices sin aristas incidentes o de salida
        for u in self.vertices:
            for v in u.vecinos:
                G.add_edge(u.clave,v[0].clave)
        nx.draw_circular(G,with_labels=True)
        plt.show()

    def buscarNodo(self,clave):
        for u in self.vertices:
            if u.clave == clave:
                return u
        return None

    def mostrarPadres(self):
        for u in self.vertices:
            print("Vertice",u.clave,": ",end="")
            if u.pi == None:
                print("None",end="")
            else:
                print(u.pi.clave," ",end="")
            print("")

    def mostrarGrafoSimplificado(self):
        G = nx.DiGraph()
        for u in self.vertices:
            G.add_node(u.clave) #para mostrar vértices sin aristas incidentes o de salida
        for u in self.vertices:
            if u.pi != None:
                G.add_edge(u.pi.clave,u.clave)
        nx.draw_circular(G,with_labels=True)
        plt.show()


    def DFS_Visita(self,u):
        global tiempo
        global lista_enlazada
        global es_aciclico
        tiempo += 1
        u.d = tiempo
        u.color = "GRIS"
        for v in u.vecinos:
            if v[0].color == "GRIS":
                es_aciclico = False
            if v[0].color == "BLANCO":
                v[0].pi = u
                self.DFS_Visita(v[0])
        u.color = "NEGRO"
        lista_enlazada.append(u)
        tiempo += 1
        u.f = tiempo

    def DFS(self):
        c=0
        global lista_enlazada
        global noconectado
        global tiempo
        global es_aciclico
        noconectado=False
        for u in self.vertices:
            u.color = "BLANCO"
            u.pi = None
        tiempo = 0
        es_aciclico=True
        for u in self.vertices:
            if u.color == "BLANCO":
                c=c+1
                print("Se selecciono:",u.clave)
                self.DFS_Visita(u)
        if c>1:
            noconectado=True
        return lista_enlazada
