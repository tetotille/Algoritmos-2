#Cada centrífuga tiene C cámaras, y cada cámara puede tener 0, 1 o 2 muestras
from sys import stdin

class Contenedor():
    def __init__(self, numero = -1, lista_especimenes = []):
        self.numero = numero
        self.lista_especimenes = lista_especimenes

    def agregar_especimen(self,especimen):
        if len(self.lista_especimenes)==2:
            return False#false cuando la lista está completa
        self.lista_especimenes.insert(0,especimen)
        return True#True si se añadió a la lista

    def __str__(self):
        especimenes_str = ""
        for especimen in self.lista_especimenes:
            especimenes_str+=str(especimen)+" "
        return " "+str(self.numero)+": "+especimenes_str

    def retornar_CM(self):
        return sum(self.lista_especimenes)

def contenedores_solitarios(numero_contenedores, lista_contenedores, lista_masas):
    n = 2 * numero_contenedores - len(lista_masas)
    numero_masas = len(lista_masas)
    for i in range(n):
        if len(lista_masas)==0:
            break

        else:
            lista_contenedores.append(Contenedor(i, [lista_masas.pop()]))
    m = numero_contenedores - numero_masas
    if m > 0 :
        for i in range(m):
            lista_contenedores.append(Contenedor(i+len(lista_contenedores),[]))

    return n, numero_contenedores-n, lista_contenedores, lista_masas

####Entrada de tipo archivo txt
arr = []
for x in stdin.readlines():
    arr.append(x)
n = len(arr)

###Algoritmo
for i in range(0,n,2):
    numero_contenedores = int(arr[i][0])
    lista_masas = arr[i+1].split()
    lista_masas = [int(x) for x in lista_masas]
    lista_aux = lista_masas.copy()
    lista_masas.sort()
    lista_contenedores = []
    n, numero_contenedores, lista_contenedores, lista_masas = contenedores_solitarios(numero_contenedores, lista_contenedores, lista_masas)
    for j in range(2):
        for k in range(numero_contenedores):
            if len(lista_masas)==0 and j == 0:
                lista_contenedores.append(Contenedor(n+k))
            elif j == 0:
                lista_contenedores.append(Contenedor(n+k,[lista_masas.pop()]))
            elif len(lista_masas) != 0:
                lista_contenedores[n+k].agregar_especimen(lista_masas.pop(0))
        if len(lista_masas)==0: break
    AM = (sum(lista_aux))/len(lista_contenedores)
    print("Set #"+str(int(i/2+1)),end="")
    imbalance = 0.00000
    for contenedor in lista_contenedores:
        imbalance = imbalance + abs(contenedor.retornar_CM() - AM)
        print("\n"+str(contenedor),end="")
    print("\nIMBALANCE = "+str(imbalance)+"0000\n\n\n")
